<template>
    <div id="static-set-form">
        <div><button @click="onSubmit">{{submitButtonText()}}</button></div>
        <label>
            <input v-model="newSetId" placeholder="set id"/>
        </label><br>
        <label>
            <input v-model="source" placeholder="source"/>
        </label>
        <TextImagePasteCollector v-model="instructions" placeholder="instructions"/>
        <TextImagePasteCollector v-model="questions" placeholder="questions"/>
        <TextImagePasteCollector v-model="answers" placeholder="answer pages"/>
    </div>
</template>

<script lang="ts">
    import Component from "vue-class-component";
    import {Prop, Vue} from "vue-property-decorator";
    import TextImagePasteCollector from "@/components/TextImagePasteCollector.vue";
    import {StaticProblemSetFormInfo, TextOrImage} from "@/store";
    import {StaticAPI} from "@/api/staticApi";


    @Component({
        components: {
            TextImagePasteCollector
        }
    })
    export default class StaticSetForm extends Vue {
        @Prop() public setId: string | undefined;

        public instructions: Array<TextOrImage> = [];

        public questions: Array<TextOrImage> = [];

        public answers: Array<TextOrImage> = [];

        public newSetId: string = "";

        public source: string = "";

        private staticApi: StaticAPI = new StaticAPI();

        submitButtonText() {
            return this.setId == null ? "create" : "submit"
        }

        onSubmit() {
            let formInfo: StaticProblemSetFormInfo = {
                instructions: this.instructions,
                problems: this.questions,
                answers: this.answers,
                source: this.source,
                id: this.newSetId,
            };

            this.staticApi.createStaticProblemSet(formInfo);
        }
    }
</script>

<style scoped>

</style>
