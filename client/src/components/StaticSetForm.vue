<template>
    <div id="static-set-form">
        <label>
            <input v-model="newSetId" placeholder="problem set id"/>
        </label>
        <TextImagePasteCollector></TextImagePasteCollector>
    </div>
</template>

<script lang="ts">
    import Component from "vue-class-component";
    import {Prop, Vue} from "vue-property-decorator";
    import TextImagePasteCollector from "@/components/TextImagePasteCollector.vue";


    @Component({
        components: {
            TextImagePasteCollector
        }
    })
    export default class StaticSetForm extends Vue {
        @Prop() public setId: string | undefined;

        public newSetId: string = "";

        // protected async mounted() {
        //
        // }
    }
</script>

<style scoped>

</style>