<template>
    <div>
        <div :key="widgetsKey">
            <div class="widget-list" v-for="(widget, i) in widgets" :key="i">
                <component class="widget" v-bind:is="widgetType(widget)"
                           :widget="widget"></component>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue, Watch} from "vue-property-decorator";

    import {Widget, WidgetOptions} from "@/store";

    import TextWidget from "./widgets/TextWidget.vue";
    import ImageWidget from "@/components/widgets/ImageWidget.vue";

    @Component({
        components: {}
    })
    export default class WidgetList extends Vue {
        @Prop() public widgets!: Array<Widget>;

        widgetsKey = 0;

        widgetType(widget: Widget) {
            let options: WidgetOptions = widget.options;
            if (options.type === "image") {
                return ImageWidget;
            } else if (options.type === "text") {
                return TextWidget;
            }
        }

        @Watch('widgets')
        onWidgetsChanged() {
            this.widgetsKey++;
        }
    }
</script>
<style scoped lang="scss">
    .widget-list > * {
        margin-bottom: 1em;
    }

    .widget-list:last-child > * {
        margin-bottom: 0;
    }
</style>