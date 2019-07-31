<template>
    <div id="static-set-form">
        <label>
            <input v-model="newSetId" placeholder="problem set id"/>
        </label>
        <TextImagePasteCollector v-model="instructions" placeholder="paste set instructions"/>
        <TextImagePasteCollector v-model="problems" placeholder="paste questions"/>
        <TextImagePasteCollector v-model="answers" placeholder="paste answer pages"/>
    </div>
</template>

<script lang="ts">
    import Component from "vue-class-component";
    import {Prop, Vue} from "vue-property-decorator";
    import TextImagePasteCollector from "@/components/TextImagePasteCollector.vue";
    import {BlobUrlPair} from "@/store";


    @Component({
        components: {
            TextImagePasteCollector
        }
    })
    export default class StaticSetForm extends Vue {
        @Prop() public setId: string | undefined;

        public instructions: Array<BlobUrlPair> = [];

        public newSetId: string = "";
    }
</script>

<style scoped>

</style>