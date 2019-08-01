<template>
    <div id="manage-static">
        <router-view></router-view>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator';

    @Component({})
    export default class ManageStatic extends Vue {}
</script>
