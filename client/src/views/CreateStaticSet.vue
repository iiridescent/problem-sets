<template>
    <div id="create-static-set">
        <StaticSetForm></StaticSetForm>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator';
    import StaticSetForm from "@/components/StaticSetForm.vue";

    @Component({
        components: {
            StaticSetForm
        },
    })
    export default class CreateStaticSet extends Vue {}
</script>

<style scoped>
    #create-static-set {
        left: 0;
        right: 0;
        margin: 0 auto;
        max-width: 700px;
    }
</style>
