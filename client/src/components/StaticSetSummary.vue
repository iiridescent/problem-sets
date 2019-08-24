<template>
    <div class="card" :class="{ 'selected-card': selected }" id="static-set-summary" @click="onClick">
        <div class="summary-info"><p>{{set.id}}</p>
            <p><b>source:</b> {{set.source}}</p></div>
        <div class="summary-actions">
            <button class="btn btn-sm" v-clipboard:copy="set.id">copy id <p class="shortcut" :class="{ 'shortcut-disabled': !selected }"><span>ctrl</span>+<span>c</span></p></button>
            <button class="btn btn-sm" @click="onClickDelete()">{{getDeleteText()}}<p class="shortcut" :class="{ 'shortcut-disabled': !selected }"><span>ctrl</span>+<span>del</span></p></button>
        </div>
    </div>
</template>

<script lang="ts">
    import { StaticProblemSet } from "@/store";
    import Component from "vue-class-component";
    import { Prop, Vue, Watch } from "vue-property-decorator";

    @Component({})
    export default class StaticSetSummary extends Vue {
        @Prop() public set: StaticProblemSet | undefined;
        @Prop() public onDeleteCallback: Function | undefined;
        @Prop() public onClickCallback: Function | undefined;
        @Prop() public selected: Boolean = false;

        public hasClickedDeleteOnce = false;

        onClickDelete() {
            if (!this.hasClickedDeleteOnce) {
                this.hasClickedDeleteOnce = true;
                return;
            }

            if (!this.onDeleteCallback || !this.set) {
                return;
            }

            this.onDeleteCallback(this.set.id);
        }

        onClick() {
            if (!this.onClickCallback || !this.set) {
                return;
            }

            this.onClickCallback(this.set.id)
        }

        getDeleteText() {
            return this.hasClickedDeleteOnce ? "click again to delete" : "delete";
        }

        @Watch('selected')
        onSelectedStateChanged() {
            this.$forceUpdate();
        }
    }
</script>

<style scoped>
    /*.delete {*/
    /*    font-weight: bold;*/
    /*}*/

    /*.delete:hover {*/
    /*    cursor: pointer;*/
    /*    user-select: none;*/
    /*    text-decoration: underline;*/
    /*}*/

    /*.copy {*/
    /*    font-weight: bold;*/
    /*}*/

    #static-set-summary {
        padding: 12pt;
        display: flex;
    }

    .summary-info {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }

    .summary-actions {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        margin-left: 12pt;
    }

    .summary-actions > * {
        margin-bottom: 8pt;
    }

    .summary-actions > :last-child {
        margin-bottom: 0;
    }

    .summary-info > :first-child {
        margin-top: 0;
    }

    .summary-info > :last-child {
        margin-bottom: 0;
    }

    .summary-info > * {
        margin: 10pt 0;
    }
</style>
