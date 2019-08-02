<template>
    <div class="wrapper">
        <div class="info-controls">
            <div class="problemNumber">{{ problemNumber }}.</div>
            <div class="answer-visible-button" @click="toggleAnswerVisibility">{{ showingAnswer ? "hide" : "show" }}
            </div>
        </div>
        <div class="content">
            <div v-if="isStatic">
                <div v-if="!staticSet">loading instructions...</div>
                <div v-else>
                    <WidgetList :widgets="staticSet.instructionContents"/>
                </div>
            </div>
            <WidgetList :widgets="problem.content"/>
            <div class="answer" v-show="showingAnswer">
                <hr class="divider">
                <div v-if="staticSet != null">{{staticSet.source}}</div>
                <WidgetList :widgets="answerWidgets()"/>
                <div class="problem-info">
                    <p>{{problem.format}}</p>
                    <p>set id: {{problem.setId}}</p>
                    <p>id: {{getId()}} <span class="copy" v-clipboard:copy="getId()">(copy)</span></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import {StaticAPI} from "@/api/staticApi";
    import WidgetList from "@/components/WidgetList.vue";
    import ImageWidget from "@/components/widgets/ImageWidget.vue";

    import {GeneratedProblem, StaticProblem, Widget, WidgetOptions, StaticProblemSet} from "@/store";
    import {Component, Prop, Vue, Watch} from "vue-property-decorator";

    import TextWidget from "./widgets/TextWidget.vue";

    @Component({
        components: {WidgetList}
    })
    export default class ProblemCard extends Vue {
        @Prop() public problem!: GeneratedProblem | StaticProblem;
        @Prop() public problemNumber!: number;

        public showingAnswer: boolean = false;
        public staticSet: StaticProblemSet | null = null;
        public isStatic: Boolean = false;
        public staticApi: StaticAPI = new StaticAPI();


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

            if (this.staticSet != null) {
                this.staticApi.setProblemUsed(this.problem.id, true)
            }
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
            return this.staticSet != null ? this.staticSet.answerContents : (this.problem as GeneratedProblem).solution
        }

        public getId() {
            return this.staticSet != null ? this.problem.id : `${this.problem.setId}:${this.problem.id}`
        }

        @Watch('problem')
        onProblemChanged() {
            this.setupStatic();
        }
    }
</script>
<style scoped lang="scss">
    .content {
        line-height: 1;
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
        border-radius: 4pt;
        box-shadow: 0 4px 0 #dadada;
        background-color: #f5f5f5;
    }

    @media only screen and (min-width: 948px) {
        .wrapper {
            width: 900px
        }
    }

    .info-controls {
        flex: 2;
    }

    @media only screen and (min-width: 600px) {
        .info-controls {
            flex: 1;
        }
    }

    .problemNumber {
        font-size: 1.25em;
        padding: 4pt 6pt;
        height: min-content;
        text-align: center;
        font-weight: bold;
    }

    .divider {
        height: 0px;
        padding: 0;
        margin: 12pt 8pt;
        border: 1px solid #212121;
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

    .problem-info *:last-child {
        margin-bottom: 0;
    }

    @media only screen and (max-width: 500px) {
        .problem-info {
            line-height: 0.5;
        }
    }

    .copy {
        cursor: pointer;
        user-select: none;
    }

    .copy:hover {
        text-decoration: underline;
    }

    .copy:active {
        color: #444444;
    }
</style>
