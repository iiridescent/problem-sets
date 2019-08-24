<template>
    <div ref="text"></div>
</template>

<script lang="ts">
    import { Component, Prop, Vue, Watch } from "vue-property-decorator";
    import renderMathInText from "@/util/render-text/render-text";

    @Component({})
    export default class MathText extends Vue {
        // need to be formatting latex with katex here
        @Prop() public text!: string;

        mounted() {
            this.renderText();
        }

        renderText() {
            const textElement = this.$refs["text"] as Element;

            textElement.innerHTML = "";

            textElement.appendChild(renderMathInText(this.text) as unknown as Node);
        }

        @Watch('text')
        onTextUpdated() {
            this.renderText();
            console.log('updating text')
        }
    }
</script>
