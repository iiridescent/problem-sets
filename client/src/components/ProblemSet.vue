<template>
    <div id="problem-set">
        <div v-show="problems.length + errors.length === 0">Loading...</div>
        <div class="card-holder" v-if="problems.length + errors.length > 0" :key="updateCount">
            <div v-for="(problem, i) in problems" :key="i">
                <div v-bind:id="selectedSetIndex === i ? 'selected-set' : undefined" tabindex=0
                     :ref="selectedSetIndex === i ? 'selected' : null">
                    <ProblemCard :selected="selectedSetIndex === i" :problem="problem"
                                 :problemNumber="problems.length > 1 ? i : null" :onClickCallback="selectProblem"/>
                </div>
            </div>
            <div v-for="(error, i) in errors" :key="i">
                <MessageCard>{{error.message}}</MessageCard>
            </div>
        </div>
        <button id="reload-button" class="btn btn-lg float-bottom-right" @click="load">
            reload<p class="shortcut"><span>r</span></p>
        </button>
    </div>
</template>
<script lang="ts">
    import MessageCard from "@/components/MessageCard.vue";
    import { Problem } from "@/store";
    import { Component, Prop, Vue } from "vue-property-decorator";

    import { ProblemSetsAPI } from "@/api/problemSetsApi";

    import ProblemCard from "./ProblemCard.vue";

    @Component({
                   components: {
                       MessageCard,
                       ProblemCard
                   }
               })
    export default class ProblemSet extends Vue {
        @Prop() public types!: string[];
        @Prop() public count!: number;

        public problems: Array<Problem> = [];
        public errors: Array<Error> = [];
        problemSetsApi: ProblemSetsAPI = new ProblemSetsAPI();

        public updateCount = 0;

        public selectedSetIndex = 0;
        public lastSetIndex = -1;
        public needsFocus = true;

        protected async mounted(): Promise<void> {
            this.load();
        }

        protected updated() {
            this.updateFocus();
        }

        public updateFocus() {
            if (!this.problems || this.problems.length === 0) {
                return;
            }

            if (this.needsFocus) {
                console.log((this.$refs.selected as Element[] | Vue[])[0]);
                this.$nextTick(() => ((this.$refs.selected as Element[] | Vue[])[0] as HTMLElement).focus());
            }
        }

        protected created() {
            window.addEventListener("keydown", this.onKeyDown);
        }

        protected destroyed() {
            window.removeEventListener("keydown", this.onKeyDown);
        }

        public onKeyDown(e: KeyboardEvent) {
            // r
            if (e.keyCode === 82) {
                this.load();
                e.preventDefault();
                return false;
            }

            if (!this.problems || this.problems.length === 0) {
                return true;
            }

            // up
            if (e.keyCode === 38) {
                this.onUp();
                e.preventDefault();
                return false;
            }

            // down
            if (e.keyCode === 40) {
                this.onDown();
                e.preventDefault();
                return false;
            }

            // home
            if (e.key == "Home") {
                this.selectProblem(0);
                e.preventDefault();
                return false;
            }

            // end
            if (e.key == "End") {
                this.selectProblem(this.problems.length - 1);
                e.preventDefault();
                return false;
            }

            // page up
            if (e.key == "PageUp") {
                this.incrementSelected(-5);
                e.preventDefault();
                return false;
            }

            // page down
            if (e.key == "PageDown") {
                this.incrementSelected(5);
                e.preventDefault();
                return false;
            }

            return true;
        }

        isError(value: any) {
            return value instanceof Error;
        }

        async load() {
            let count = this.count != null ? this.count : 1;

            const problemsAndErrors: Array<Problem | Error> = await this.problemSetsApi.loadProblemsOfTypes(this.types, count);
            this.errors = problemsAndErrors.filter((problemOrError) => this.isError(problemOrError)) as Error[];
            this.problems = problemsAndErrors.filter((problemOrError) => !this.isError(problemOrError)) as Problem[];
            this.updateCount += 1;
        }

        public onUp() {
            console.log("up");

            this.incrementSelected(-1);
        }

        public onDown() {
            console.log("down");

            this.incrementSelected(1);
        }

        public incrementSelected(i: number) {
            this.selectProblem(this.selectedSetIndex + i);
        }

        public selectProblem(i: number) {
            if (!this.problems || this.problems.length == 0) {
                return;
            }

            const newSetIndex = Math.max(Math.min(i, this.problems.length - 1), 0);

            if (i === this.selectedSetIndex) {
                return;
            }

            this.lastSetIndex = this.selectedSetIndex;
            this.selectedSetIndex = newSetIndex;
            this.needsFocus = true;
        }
    }
</script>

<style scoped lang="scss">
    #problem-set {
        left: 0;
        right: 0;
        max-width: 900px;
        margin: 0 auto;
    }

    .float-bottom-right {
        position: fixed;
        right: 10pt;
        bottom: 10pt;
    }
</style>
