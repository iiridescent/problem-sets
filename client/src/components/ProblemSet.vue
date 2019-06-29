<template>
  <div class="wrapper">
    <div v-show="problems.length == 0">Loading...</div>
    <div class="problem-set" v-if="problems.length > 0">
      <div v-for="(problem, i) in problems" :key="i">
        <ProblemCard v-bind:problem="problems[i]" :problemNumber="i+1"/>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { Problem } from "@/store";
import { Component, Prop, Vue } from "vue-property-decorator";

import { ProblemSetsAPI } from "../api/problemSetsApi";

import ProblemCard from "./ProblemCard.vue";

@Component({
  components: {
    ProblemCard
  }
})
export default class ProblemSet extends Vue {
  @Prop() public types!: string[];

  public problems: Problem[] = [];

  protected async mounted(): Promise<void> {
    const problemSetsApi: ProblemSetsAPI = new ProblemSetsAPI();

    console.log(this.types);

    this.problems = await problemSetsApi.loadProblemsOfTypes(this.types);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.problem-set {
  // display: flex;
  // flex-wrap: wrap;
  left: 0;
  right: 0;
  margin: 0 auto;
}

.problem-set > * {
  padding: 12pt 0pt;
}

.wrapper {
  left: 0;
  right: 0;
  margin: 0 auto;
}
</style>
