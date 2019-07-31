<template>
    <div>
        <input @keyup.ctrl.enter="onSubmit" @paste="onPaste" v-model="textValue" v-bind:placeholder="placeholder"/>
        <div class="pasted-images" v-if="items.length > 0">
            <div v-for="(item, i) in items" :key="i">
                <div v-if="itemType(item) === 'text'">
                    <h3>{{item}}</h3>
                </div>
                <div v-if="itemType(item) === 'image'">
                    <img class="pasted-image" v-bind:src="item.url"/>

                </div>
                <button class="close-button" @click="removeItem(i)"> X</button>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import { TextOrImage } from "@/store";
    import { Component, Prop, Vue } from "vue-property-decorator";

    @Component({})
    export default class TextImagePasteCollector extends Vue {
        @Prop() public placeholder: string | undefined;

        public items: Array<TextOrImage> = [];

        public textValue: string = "";

        onPaste(e: ClipboardEvent) {
            for (let i = 0; i < e.clipboardData!.items.length; i++) {

                // get the clipboard item
                let clipboardItem = e.clipboardData!.items[i];
                let type = clipboardItem.type;

                // if it's an image add it to the image field
                if (type.indexOf("image") != -1) {

                    // get the image content and create an img dom element
                    let blob = clipboardItem.getAsFile();

                    if (blob !== null) {
                        let blobUrl = window.URL.createObjectURL(blob);

                        this.items.push({
                                            blob: blob,
                                            url: blobUrl
                                        });

                        this.updateEvent();
                    }
                } else {
                    console.log("Not supported: " + type);
                }

            }
        }

        onSubmit() {
            if (!this.textValue) {
                return;
            }
            this.items.push(this.textValue);
            this.textValue = "";
            this.updateEvent();
        }

        removeItem(i: number) {
            if (i > -1) {
                this.items.splice(i, 1);
            }
            this.updateEvent();
        }

        updateEvent() {
            this.$emit("input", this.items);
        }

        itemType(item: TextOrImage) {
            if (typeof item == "string") {
                return "text";
            } else if (item.blob && item.url) {
                return "image";
            }

        }
    }
</script>

<style scoped lang="scss">
    .pasted-image {
        box-shadow: 0 10px 10px #888888;
    }

    .close-button {
        font-size: 2em;
        background: black;
        color: white;
        border: none;
    }
</style>
