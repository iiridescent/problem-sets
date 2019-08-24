<template>
    <MathText :text="text"></MathText>
</template>

<script lang="ts">
    import MathText from "@/components/MathText.vue";
    import { Component, Prop, Vue } from "vue-property-decorator";

    import { TextWidgetOptions, Widget } from "@/store";

    @Component({
                   components: {
                       MathText
                   }
               })
    export default class TextWidget extends Vue {
        @Prop() public widget!: Widget;

        private text: String = "";

        mounted() {
            const options: TextWidgetOptions = this.widget.options as TextWidgetOptions;

            this.text = options.text;
        }
    }
</script>
