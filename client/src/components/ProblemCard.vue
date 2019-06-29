<template>
  <div class="wrapper">
    <div class="info-controls">
      <div class="number">{{ problemNumber }}.</div>
      <div class="answer-visible-button" @click="toggleAnswerVisibility">{{ showingAnswer ? "hide" : "show" }}</div>
    </div>
    <div class="problems">
      <div v-for="(problemContent, i) in problem.content" :key="i">
        <component class="widget" v-bind:is="textWidgetComponent()" :widget="problemContent"></component>
      </div>
      <div class="answer" v-show="showingAnswer">
        <hr class="divider">
        <div v-for="(problemSolution, i) in problem.solution" :key="i">
          <component class="widget" v-bind:is="textWidgetComponent()" :widget="problemSolution"></component>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

import { Problem } from "../store";

import TextWidget from "./widgets/TextWidget.vue";

@Component({
  components: {}
})
export default class ProblemCard extends Vue {
  @Prop() public problem!: Problem;
  @Prop() public problemNumber!: number;

  public showingAnswer: boolean = false;

  textWidgetComponent() {
    return TextWidget;
  }

  toggleAnswerVisibility() {
    this.showingAnswer = !this.showingAnswer;
  }
}
</script>
<style scoped lang="scss">
.problems {
  line-height: 1;
  // left: 0;
  // right: 0;
  // margin: 0 auto;
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
  box-shadow: 0px 4px 0px 0px rgba(255, 255, 255, 0.2);
  background-color: #212121;
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