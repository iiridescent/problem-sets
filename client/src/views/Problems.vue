<template>
  <div>
    <ProblemSet :types="$route.params.type.split(',')" :count="$route.params.count"/>
  </div>
</template>

<script lang="ts">
// tslint:disable-next-line:no-submodule-imports no-implicit-dependencies
import ProblemSet from "@/components/ProblemSet.vue"; // @ is an alias to /src
import { Component, Vue } from "vue-property-decorator";

@Component({
  components: {
    ProblemSet
  }
})
export default class Problems extends Vue {}
</script>