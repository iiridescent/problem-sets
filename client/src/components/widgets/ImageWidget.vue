<template>
    <div>
        <img @click="toggleExpanded()" v-bind:src="`http://${hostname}:5000/static/images/`+imageId+'.png'"/>
        <div class="expanded-background" v-if="expanded">
            <img class="expanded" @click="toggleExpanded()"
                 v-bind:src="`http://${hostname}:5000/static/images/`+imageId+'.png'"/>
        </div>
    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue} from "vue-property-decorator";

    import {ImageWidgetOptions, Widget} from "../../store";

    @Component
    export default class ImageWidget extends Vue {
        // need to be formatting latex with katex here
        @Prop() public widget!: Widget;

        public imageId: string = "";
        public hostname: string = window.location.hostname;

        expanded = false;

        mounted() {
            const options: ImageWidgetOptions = this.widget.options as ImageWidgetOptions;

            this.imageId = options.id
        }

        toggleExpanded() {
            this.expanded = !this.expanded
        }
    }
</script>
<style scoped>
    img {
        max-width: 100%;
    }

    .expanded {
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        bottom: 0;
        margin: auto;
    }

    .expanded-background {
        top: 0;
        right: 0;
        left: 0;
        bottom: 0;
        position: fixed;
        background-color: black;
        height: 100vh;
        width: 100vw;
    }
</style>
