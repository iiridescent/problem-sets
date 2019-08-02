<template>
    <div class="wrapper">
        <div class="info-controls">
            <div class="warning">
                🤨&#xFE0F;
            </div>
        </div>
        <div class="content">
            <p>
                <slot></slot>
            </p>
        </div>
    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue} from "vue-property-decorator";

    @Component({})
    export default class SetCard extends Vue {
        @Prop() public number!: number;
    }
</script>
<style scoped lang="scss">
    .content {
        line-height: 1;
        flex: 10;
        width: 100%;
        padding: 0 8pt;
        display: inline-block;
        transition: height 200ms;
    }

    .content > * {
        padding: 8pt;
        width: 100%;
    }


    .answer > * {
        padding: 8pt;
    }

    .wrapper {
        display: flex;
        flex-direction: row;
        padding: 12pt;
        border-radius: 4pt;
        box-shadow: 0 4px 0 #dadada;
        background-color: #f5f5f5;
    }

    @media only screen and (min-width: 948px) {
        .wrapper {
            width: 900px
        }
    }

    .info-controls {
        flex: 2;
    }

    @media only screen and (min-width: 600px) {
        .info-controls {
            flex: 1;
        }
    }

    .warning {
        font-size: 2em;
        text-align: center;
        font-family: "Noto", sans-serif;
        font-weight: bold;
        height: 100%;
        display: flex;
        justify-content: center;
        flex-direction: column;
    }
</style>
