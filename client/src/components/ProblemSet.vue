<template>
    <div class="wrapper">
        <div v-show="problems.length == 0">Loading...</div>
        <div class="problem-set" v-if="problems.length > 0">
            <div v-for="(problem, i) in problems" :key="i">
                <div v-if="isError(problem)">
                    <MessageCard>{{problem.message}}</MessageCard>
                </div>
                <div v-else>
                    <ProblemCard :problem="problems[i]" :problemNumber="i+1"/>
                </div>
            </div>
        </div>
        <div id="reload-button" class="float-bottom-right" @click="load">
            🔄
        </div>
    </div>
</template>
<script lang="ts">
    import {Problem} from "@/store";
    import {Component, Prop, Vue} from "vue-property-decorator";

    import {ProblemSetsAPI} from "../api/problemSetsApi";

    import ProblemCard from "./ProblemCard.vue";
    import MessageCard from "@/components/MessageCard.vue";

    @Component({
        components: {
            MessageCard,
            ProblemCard
        }
    })
    export default class ProblemSet extends Vue {
        @Prop() public types!: string[];
        @Prop() public count!: number;

        public problems: Array<Problem | Error> = [];
        problemSetsApi: ProblemSetsAPI = new ProblemSetsAPI();

        protected async mounted(): Promise<void> {
            this.load()
        }

        isError(value: any) {
            return value instanceof Error
        }

        async load() {
            let count = this.count != null ? this.count : 1;

            this.problems = await this.problemSetsApi.loadProblemsOfTypes(this.types, count);
            this.$forceUpdate();
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
        padding: 12pt 0;
    }

    @media only screen and (max-width: 748px) {
        .problem-set > * {
            padding: 6pt 0;
        }
    }

    .wrapper {
        left: 0;
        right: 0;
        margin: 0 auto;
    }

    .float-bottom-right {
        position: fixed;
        right: 10pt;
        bottom: 10pt;
    }

    #reload-button {
        font-size: 2em;
        transition: 500ms transform;
        cursor: pointer;
        user-select: none;
    }

    #reload-button:hover {
        transform: rotate(-180deg) translate(0, -0.12em);
    }
</style>
