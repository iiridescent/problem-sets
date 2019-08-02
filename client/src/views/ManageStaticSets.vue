<template>
    <div id="manage-static-sets">
        <div v-if="sets != null && sets.length > 0">
            <div v-for="(set, i) in sets" :key="i">
                <p>{{set.id}} <span class="x-button" @click="removeSet(set.id)">(delete)</span></p>
                <p><b>source:</b> {{set.source}}</p><br>
            </div>
        </div>
        <div v-else>
            <h1>Ø no static problem sets</h1>
        </div>
    </div>
</template>

<script lang="ts">
    import {Component, Vue} from 'vue-property-decorator';
    import {StaticAPI} from "@/api/staticApi";
    import {StaticProblemSet} from "@/store";

    @Component({})
    export default class ManageStaticSets extends Vue {
        public staticApi = new StaticAPI();
        public sets: StaticProblemSet[] | null = null;

        protected async mounted() {
            this.loadSets()
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
            await this.staticApi.deleteStaticProblemSet(id)
            this.loadSets()
        }
    }
</script>

<style scoped lang="scss">
    .x-button {
        font-weight: bold;
        color: darkred;
    }

    .x-button:hover {
        color: red;
        cursor: pointer;
        user-select: none;
    }
</style>