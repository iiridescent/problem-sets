<template>
    <img v-bind:src="'http://localhost:5000/static/images/'+imageId+'.png'"/>
</template>

<script lang="ts">
  import {Component, Prop, Vue} from "vue-property-decorator";

  import {ImageWidgetOptions, Widget} from "../../store";

  @Component
export default class ImageWidget extends Vue {
  // need to be formatting latex with katex here
  @Prop() public widget!: Widget;

  public imageId: string = "";

  mounted() {
    const options: ImageWidgetOptions = this.widget.options as ImageWidgetOptions;

    this.imageId = options.id
  }
}
</script>
