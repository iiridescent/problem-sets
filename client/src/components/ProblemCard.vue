<template>
    <div class="wrapper card" :class="{ 'selected-card': selected }" @click="onClick">
        <div class="info-controls">
            <div class="problem-number" v-if="problemNumber != null">{{ problemNumber + 1 }}.</div>
            <button class="btn btn-sm" @click="toggleAnswerVisibility">
                {{ showingAnswer ? "hide" : "show" }}<p class="shortcut"><span>h</span></p>
            </button>
            <div v-if="showingAnswer && isStatic" class="used-toggle-container">
                <span class="used-toggle-indicator">{{markStaticAsUsed ? '\u{2705}' : '\u{274C}'}}</span>
                <button class="btn btn-sm" @click="toggleMarkStaticAsUsed()">
                    mark used <p class="shortcut"><span>g</span></p>
                </button>
            </div>
        </div>
        <div class="content">
            <div v-if="isStatic && (!staticSet || staticSet.instructionContents.length > 0)">
                <div v-if="!staticSet">loading instructions...</div>
                <div v-else-if="staticSet.instructionContents">
                    <WidgetList :widgets="staticSet.instructionContents"/>
                </div>
            </div>
            <WidgetList :widgets="problem.content"/>
            <div class="answer" v-show="showingAnswer">
                <div class="divider"></div>
                <div v-if="staticSet != null">{{staticSet.source}}</div>
                <WidgetList :widgets="answerWidgets()"/>
                <div class="divider"></div>
                <div class="problem-info">
                    <p>{{problem.format}}</p>
                    <p>set id: {{problem.setId}} <span class="copy" v-clipboard:copy="problem.setId">(copy)</span></p>
                    <p>id: {{getId()}} <span class="copy" v-clipboard:copy="getId()">(copy)</span></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import { StaticAPI } from "@/api/staticApi";
    import WidgetList from "@/components/WidgetList.vue";
    import ImageWidget from "@/components/widgets/ImageWidget.vue";

    import { GeneratedProblem, StaticProblem, Widget, WidgetOptions, StaticProblemSet } from "@/store";
    import { Component, Prop, Vue, Watch } from "vue-property-decorator";

    import TextWidget from "./widgets/TextWidget.vue";

    @Component({
                   components: {WidgetList}
               })
    export default class ProblemCard extends Vue {
        @Prop() public problem!: GeneratedProblem | StaticProblem;
        @Prop() public problemNumber!: number;
        @Prop() public onClickCallback: Function | undefined;
        @Prop() public selected!: boolean;

        public showingAnswer: boolean = false;
        public staticSet: StaticProblemSet | null = null;
        public isStatic: boolean = false;
        public staticApi: StaticAPI = new StaticAPI();
        public markStaticAsUsed: boolean = true;

        widgetType(widget: Widget) {
            let options: WidgetOptions = widget.options;
            if (options.type === "image") {
                return ImageWidget;
            } else if (options.type === "text") {
                return TextWidget;
            }
        }

        toggleAnswerVisibility() {
            this.showingAnswer = !this.showingAnswer;

            if (this.staticSet != null && this.showingAnswer && this.markStaticAsUsed) {
                this.staticApi.setProblemUsed(this.problem.id, true);
            }
        }

        toggleMarkStaticAsUsed() {
            this.markStaticAsUsed = !this.markStaticAsUsed;

            if (!this.isStatic || this.staticSet == null) {
                return;
            }



            this.staticApi.setProblemUsed(this.problem.id, this.markStaticAsUsed);
        }

        onClick() {
            if (!this.onClickCallback || this.problemNumber == null) {
                return;
            }

            this.onClickCallback(this.problemNumber);
        }

        protected created() {
            window.addEventListener("keydown", this.onKeyDown);
        }

        protected destroyed() {
            window.removeEventListener("keydown", this.onKeyDown);
        }

        public onKeyDown(e: KeyboardEvent) {
            // h
            if (e.keyCode === 72 && this.selected) {
                this.toggleAnswerVisibility();
                e.preventDefault();
                return false;
            }

            if (e.keyCode == 71 && this.selected && this.isStatic) {
                this.toggleMarkStaticAsUsed();
                e.preventDefault();
                return false;
            }

            return true;
        }

        protected async beforeMount() {
            this.setupStatic();
        }

        async setupStatic() {
            if (this.problem.format != "static") {
                return;
            }

            this.isStatic = true;

            let staticSetOrError: StaticProblemSet | string = await this.staticApi.getStaticProblemSet(this.problem.setId);

            if (typeof (staticSetOrError) !== "string" && staticSetOrError.id) {
                this.staticSet = staticSetOrError;
            }
        }

        public answerWidgets() {
            return this.staticSet != null ? this.staticSet.answerContents : (this.problem as GeneratedProblem).solution;
        }

        public getId() {
            return this.staticSet != null ? this.problem.id : `${this.problem.setId}:${this.problem.id}`;
        }

        @Watch("problem")
        onProblemChanged() {
            this.setupStatic();
            this.showingAnswer = false;
        }
    }
</script>
<style scoped lang="scss">
    @import "../style/constants";

    .content {
        flex: 10;
        width: 100%;
        padding: 0 8pt;
        display: inline-block;
        transition: height 200ms;
    }

    .content > * {
        padding: 8pt;
        width: 100%;
    }

    .content .answer {
        padding: 0;
        width: 100%;
    }

    .answer > * {
        padding: 8pt;
    }

    .wrapper {
        display: flex;
        flex-direction: row;
        padding: 12pt;
        width: calc(100% - 34px);
    }

    /*@media only screen and (min-width: 948px) {*/
    /*    .wrapper {*/
    /*        width: 900px*/
    /*    }*/
    /*}*/

    .info-controls {
        width: 60pt;
    }

    @media only screen and (min-width: 600px) {
        .info-controls {
            width: 90pt
        }
    }

    .info-controls > * {
        width: 100%;
        margin-bottom: 8pt;
    }

    .info-controls > *:last-child {
        margin-bottom: 0;
    }

    .problem-number {
        font-size: 1.25em;
        padding: 4pt 6pt;
        height: min-content;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10pt;
    }

    .divider {
        height: 1px;
        padding: 0;
        background-color: $primary-darker;
        margin: 12pt -20pt 12pt 8pt
    }

    .answer-visible-button {
        transition: opacity 200ms;
        user-select: none;
        text-align: center;
    }

    .answer-visible-button:hover {
        opacity: 0.5;
        cursor: pointer;
    }

    .problem-info {
        margin: 0;
        text-transform: lowercase;
        font-family: sans-serif;
        /*font-style: italic;*/
        font-size: 0.9em;
        color: #888888;
    }

    .problem-info > *:first-child {
        margin-top: 0;
    }

    .problem-info > *:last-child {
        margin-bottom: 0;
    }

    .used-toggle-container {
        display: flex;
        align-items: center;
    }

    .used-toggle-container .used-toggle-indicator {
        margin-right: 8pt;
    }
</style>
