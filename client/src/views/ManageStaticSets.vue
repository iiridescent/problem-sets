<template>
    <div id="manage-static-sets">
        <div class="sets-list" v-if="sets != null && sets.length > 0">
            <div v-for="(set, i) in sets" :key="i" class="card-holder">
                <div v-bind:id="selectedSetIndex === i ? 'selected-set' : undefined" tabindex=0
                     :ref="selectedSetIndex === i ? 'selected' : null">
                    <StaticSetSummary :set="set" :selected="selectedSetIndex === i"
                                      :onDeleteCallback="removeSet" :onClickCallback="selectSetById"/>
                </div>
            </div>
        </div>
        <div v-else>
            <h1>Ø no static problem sets</h1>
        </div>
    </div>
</template>

<script lang="ts">
    import StaticSetSummary from "@/components/StaticSetSummary.vue";
    import { Component, Vue } from "vue-property-decorator";
    import { StaticAPI } from "@/api/staticApi";
    import { StaticProblemSet } from "@/store";
    import { VueStatic } from "vue-scrollto";
    import * as VueScrollTo from "vue-scrollto";

    @Component({components: {StaticSetSummary}})
    export default class ManageStaticSets extends Vue {

        public staticApi = new StaticAPI();
        public sets: StaticProblemSet[] | null = null;

        public selectedSetIndex = 0;
        public lastSetIndex = -1;
        public needsFocus = true;
        $copyText: any;

        protected async mounted() {
            this.loadSets();

            this.selectSet(0);
        }

        public async loadSets() {
            let response: StaticProblemSet[] | string = await this.staticApi.getStaticProblemSets();

            if (typeof (response) === "string") {
                console.log(response);
                return;
            }

            this.sets = response;
        }

        public async removeSet(id: string) {
            if (this.staticApi == null) {
                return;
            }
            await this.staticApi.deleteStaticProblemSet(id);
            this.loadSets();
        }

        protected updated() {
            this.updateFocus();
        }

        public updateFocus() {
            if (this.needsFocus) {
                console.log((this.$refs.selected as Element[] | Vue[])[0]);
                this.$nextTick(() => ((this.$refs.selected as Element[] | Vue[])[0] as HTMLElement).focus());
            }
        }

        protected created() {
            console.log("added event listener for keyup");
            window.addEventListener("keydown", this.onKeyDown);
        }

        protected destroyed() {
            window.removeEventListener("keydown", this.onKeyDown);
        }

        public onKeyDown(e: KeyboardEvent) {
            console.log("onKeyDown, code " + e.keyCode);

            if (e.keyCode === 38) {
                this.onUp();
                e.preventDefault();
                return false;
            } else if (e.keyCode === 40) {
                this.onDown();
                e.preventDefault();
                return false;
            } else if (e.keyCode === 67 && e.ctrlKey) {
                this.copyCurrentId();
                e.preventDefault();
                return false;
            }

            if (!this.sets || this.sets.length === 0) {
                return true;
            }

            if (e.key == "Home") {
                this.selectSet(0);
                e.preventDefault();
                return false;
            } else if (e.key == "End") {
                this.selectSet(this.sets.length - 1);
                e.preventDefault();
                return false;
            } else if (e.key == "Delete" && e.ctrlKey) {
                this.removeSet(this.sets[this.selectedSetIndex].id);
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

        public onUp() {
            console.log("up");

            this.incrementSelected(-1);
        }

        public onDown() {
            console.log("down");

            this.incrementSelected(1);
        }

        public copyCurrentId() {
            if (!this.sets || this.sets.length == 0) {
                return;
            }

            this.$copyText(this.sets[this.selectedSetIndex].id);
        }

        public getSetIndexById(id: string) {
            if (!this.sets || this.sets.length == 0) {
                return;
            }

            return this.sets.findIndex((item) => item.id == id);
        }

        public incrementSelected(i: number) {
            this.selectSet(this.selectedSetIndex + i);
        }

        public selectSet(i: number) {
            if (!this.sets || this.sets.length == 0) {
                return;
            }

            const newSetIndex = Math.max(Math.min(i, this.sets.length - 1), 0);

            if (i === this.selectedSetIndex) {
                return;
            }

            this.lastSetIndex = this.selectedSetIndex;
            this.selectedSetIndex = newSetIndex;
            this.needsFocus = true;
        }

        public selectSetById(id: string) {
            const index = this.getSetIndexById(id);

            if (index == null) {
                return null;
            }

            this.selectSet(index);
        }
    }
</script>

<style scoped lang="scss">
    #manage-static-sets {
        left: 0;
        right: 0;
        margin: 0 auto;
        max-width: 700px;
    }
</style>
