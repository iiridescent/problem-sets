<template>
    <div>
        <div v-for="(widget, i) in widgets" :key="i">
            <component class="widget" v-bind:is="widgetType(widget)"
                       :widget="widget"></component>
        </div>
    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue} from "vue-property-decorator";

    import {Widget, WidgetOptions} from "@/store";

    import TextWidget from "./widgets/TextWidget.vue";
    import ImageWidget from "@/components/widgets/ImageWidget.vue";

    @Component({
        components: {}
    })
    export default class WidgetList extends Vue {
        @Prop() public widgets!: Array<Widget>;

        widgetType(widget: Widget) {
            let options: WidgetOptions = widget.options;
            if (options.type === "image") {
                return ImageWidget;
            } else if (options.type === "text") {
                return TextWidget;
            }
        }
    }
</script>
<style scoped lang="scss">

</style>