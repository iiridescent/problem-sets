<template>
    <div class="wrapper">
        <div class="info-controls">
            <div class="number">{{ problemNumber }}.</div>
            <div class="answer-visible-button" @click="toggleAnswerVisibility">{{ showingAnswer ? "hide" : "show" }}
            </div>
        </div>
        <div class="problems">
            <WidgetList :widgets="problem.content"/>
            <div v-if="!isStatic">
                <div class="answer" v-show="showingAnswer">
                    <hr class="divider">
                    <WidgetList :widgets="problem.solution"/>
                </div>
            </div>
          <div v-else>

          </div>
        </div>
    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue} from "vue-property-decorator";

    import {GeneratedProblem, StaticProblem, Widget, WidgetOptions} from "@/store";

    import TextWidget from "./widgets/TextWidget.vue";
    import ImageWidget from "@/components/widgets/ImageWidget.vue";
    import {StaticAPI} from "@/api/staticApi";
    import WidgetList from "@/components/WidgetList.vue";

    @Component({
        components: {WidgetList}
    })
    export default class ProblemCard extends Vue {
        @Prop() public problem!: GeneratedProblem | StaticProblem;
        @Prop() public problemNumber!: number;

        public showingAnswer: boolean = false;
        public isStatic: Boolean = false;
        public staticApi: StaticAPI | undefined;
        public staticSet: any | undefined;

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
        }

        mounted() {
            this.setupStatic()
        }

        setupStatic() {
            if (this.problem.format != "static") {
                return;
            }

            this.isStatic = true;
            this.staticApi = new StaticAPI()

            this.staticSet = this.staticApi.getStaticProblemSet(this.problem.setId)
        }
    }
</script>
<style scoped lang="scss">
    .problems {
        line-height: 1;
        flex: 10;
        width: 100%;
        display: inline-block;
        transition: height 200ms;
    }

    .problems > * {
        padding: 8pt;
        width: 100%;
    }

    .problems .answer {
        padding: 0;
        width: 100%;
    }

    .answer > * {
        padding: 8pt;
    }

    // .problems>*:first-child {
    //   color: red;
    // }

    .wrapper {
        display: flex;
        width: min-content;
        min-width: 600pt;
        flex-direction: row;
        padding: 12pt;
        border-radius: 4pt;
        box-shadow: 0px 4px 0px #dadada;
        background-color: #f5f5f5;
    }

    .number {
        font-size: 1.25em;
        padding: 4pt 6pt;
        height: min-content;
        text-align: center;
        font-weight: bold;
    }

    .divider {
        height: 1px;
        padding: 0;
        margin: 12pt 8pt;
        background-color: #fff;
    }

    .info-controls {
        flex: 1.5;
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
</style>