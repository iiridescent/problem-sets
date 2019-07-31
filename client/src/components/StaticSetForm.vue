<template>
    <div id="static-set-form">
        <div><button>{{submitButtonText()}}</button></div>
        <label>
            <input v-model="newSetId" placeholder="set id"/>
        </label><br>
        <label>
            <input v-model="source" placeholder="source"/>
        </label>
        <TextImagePasteCollector v-model="instructions" placeholder="instructions"/>
        <TextImagePasteCollector v-model="problems" placeholder="questions"/>
        <TextImagePasteCollector v-model="answers" placeholder="answer pages"/>
    </div>
</template>

<script lang="ts">
    import Component from "vue-class-component";
    import {Prop, Vue} from "vue-property-decorator";
    import TextImagePasteCollector from "@/components/TextImagePasteCollector.vue";
    import {TextOrImage} from "@/store";


    @Component({
        components: {
            TextImagePasteCollector
        }
    })
    export default class StaticSetForm extends Vue {
        @Prop() public setId: string | undefined;

        public instructions: Array<TextOrImage> = [];

        public problems: Array<TextOrImage> = [];

        public answers: Array<TextOrImage> = [];

        public newSetId: string = "";

        public source: string = "";

        submitButtonText() {
            return this.setId == null ? "create" : "submit"
        }
    }
</script>

<style scoped>

</style>
