<template>
    <div ref="text"></div>
</template>

<script lang="ts">
    import renderMathInText from "@/util/render-text/render-text";
    import {Component, Prop, Vue} from "vue-property-decorator";

    import {TextWidgetOptions, Widget} from "../../store";

    @Component
    export default class TextWidget extends Vue {
        // need to be formatting latex with katex here
        @Prop() public widget!: Widget;

        public text: string = "";

        mounted() {
            const options: TextWidgetOptions = this.widget.options as TextWidgetOptions;

            const textElement = this.$refs["text"] as Element;

            textElement.innerHTML = "";

            textElement.appendChild(renderMathInText(options.text) as unknown as Node);
        }
    }
</script>
