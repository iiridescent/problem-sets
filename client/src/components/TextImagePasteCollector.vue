<template>
    <div>
        <input @paste="onPaste" v-bind:placeholder=placeholder></input>
        <div class="pasted-images" v-if="images.length > 0">
            <div v-for="(image, i) in images" :key="i">
                <img class="pasted-image" v-bind:src="image.url"/>
                <button class="close-button" @click="removeImage(i)"> X </button>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import {Component, Prop, Vue} from "vue-property-decorator";
    import {BlobUrlPair} from "@/store";


    @Component({})
    export default class TextImagePasteCollector extends Vue {
        @Prop() public placeholder: string = "paste images"        
        
        public images: Array<BlobUrlPair> = [];

        onPaste(e: ClipboardEvent) {
            for (let i = 0; i < e.clipboardData!.items.length; i++) {

                // get the clipboard item
                let clipboardItem = e.clipboardData!.items[i];
                let type = clipboardItem.type;

                // if it's an image add it to the image field
                if (type.indexOf("image") != -1) {

                    // get the image content and create an img dom element
                    let blob = clipboardItem.getAsFile();

                    if (blob != null) {
                        let blobUrl = window.URL.createObjectURL(blob);

                        this.images.push({
                            blob: blob,
                            url: blobUrl
                        });

                        this.$emit('input', this.images)
                    }
                } else {
                    console.log("Not supported: " + type);
                }

            }
        }

        removeImage(i: number) {
            if (i > -1) {
                this.images.splice(i, 1);
            }
            this.$emit('input', this.images)
        }
    }
</script>

<style scoped lang="scss">
    .pasted-image {
        box-shadow: 0px 10px 10px #ab1230;
    }

    .close-button {
        font-size: 2em;
        background: black;
        color: white;
        border: none;
    }
</style>