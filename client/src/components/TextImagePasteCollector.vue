<template>
    <div id="text-image-paste-collector" @dragenter="onDragEnter" @dragover="onDragEnter" @dragexit="onDragExit" @drop="onDrop">

        <div class="input-field">
            <label>
            <textarea @keyup.ctrl.enter="onSubmitText" @paste="onPaste" v-model="inputValue"
                      v-bind:placeholder="placeholder"></textarea>
            </label>
        </div>
        <div class="divider"></div>
        <div class="content-wrapper">
            <p class="add-item-instruction shortcut-wrapper" v-if="items.length === 0"><span
                    class="shortcut"><span>ctrl</span>+<span>enter</span></span> or drag and
                drop to add item</p>
            <div class="content" v-if="items.length > 0">
                <div v-for="(item, i) in items" :key="i">
                    <div class="item-display">
                        <div class="item-content">
                            <div v-if="itemType(item) === 'text'">
                                <MathText :text="item"/>
                            </div>
                            <div v-if="itemType(item) === 'image'">
                                <img class="pasted-image card" v-bind:src="item.url"/>

                            </div>
                        </div>
                        <div class="item-actions">
                            <button class="btn btn-sm" @click="removeItem(i)">x</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="drag-modal" v-if="isDragging">
            <div class="drag-modal-center"><p class="drop-instruction">drop to upload</p></div>
        </div>
    </div>
</template>

<script lang="ts">
    import MathText from "@/components/MathText.vue";
    import { TextImagePasteCollectorState, TextOrImage } from "@/store";
    import { Component, Prop, Vue, Watch } from "vue-property-decorator";

    @Component({
                   components: {
                       MathText
                   }
               })
    export default class TextImagePasteCollector extends Vue {
        @Prop() public placeholder: string | undefined;

        public itemsAndValue: TextImagePasteCollectorState = {
            items: [],
            inputValue: ""
        };

        public inputValue: string = "";

        public items: TextOrImage[] = [];

        public isDragging: Boolean = false;

        /**
         * @returns whether the default action for the event should be prevented
         */
        async handleEventData(dataTransfer: DataTransfer) {

            console.log('event');
            console.log([...dataTransfer.items]);
            console.log([...dataTransfer.types]);
            console.log([...dataTransfer.files]);

            let shouldPreventDefault = false;
            for (let i = 0; i < dataTransfer.items.length; i++) {

                // get the clipboard item
                let item = dataTransfer.items[i];
                let type = item.type;

                // if it's an image add it to the image field
                if (type.indexOf("image") != -1) {

                    shouldPreventDefault = true;

                    // get the image content and create an img dom element
                    let file = item.getAsFile();

                    if (file !== null) {
                        let fileUrl = window.URL.createObjectURL(file);

                        this.addItem({
                                         file: file,
                                         url: fileUrl
                                     });

                        this.updateEvent();
                    }
                }

                if (type.indexOf("text/plain") != -1) {

                    const text: string = await new Promise(resolve => {
                        item.getAsString(content => resolve(content));
                    });

                    // Check if text is a valid url

                    try {
                        new URL(text);
                    } catch (_) {
                        continue;
                    }

                    const response = await fetch(text);

                    const responseBlob = await response.blob();

                    if (responseBlob == null || responseBlob.type.indexOf("image") == -1) {
                        continue;
                    }

                    // We do actually want the user to be able to paste plain text
                    // shouldPreventDefault = true;

                    let fileUrl = window.URL.createObjectURL(responseBlob);

                    let file = new File([responseBlob], "image");

                    this.addItem({
                                     file: file,
                                     url: fileUrl
                                 });

                    this.updateEvent();
                }
            }

            console.log(shouldPreventDefault);

            return shouldPreventDefault;
        }

        async onPaste(e: ClipboardEvent) {
            if (!e.clipboardData || e.clipboardData.items.length == 0) {
                return;
            }

            let shouldPreventDefault = await this.handleEventData(e.clipboardData);

            if (shouldPreventDefault) {
                e.preventDefault();

                // Prevent images from being encoded and stuck into text field
                this.clearField();
                return false;
            }

            return true;
        }

        onDragEnter(e: DragEvent) {
            this.isDragging = true;
            e.preventDefault();
            e.stopPropagation();
        }

        onDragExit(e: DragEvent) {
            this.isDragging = false;
            e.preventDefault();
            e.stopPropagation();
        }

        onDrop(e: DragEvent) {
            this.isDragging = false;

            e.preventDefault();
            e.stopPropagation();

            if (!e.dataTransfer || e.dataTransfer.items.length == 0) {
                return;
            }

            this.handleEventData(e.dataTransfer);
        }

        addItem(item: TextOrImage) {
            this.items.push(item);
            this.clearField();
            this.updateEvent();
        }

        onSubmitText() {
            if (!this.inputValue) {
                return;
            }
            this.addItem(this.inputValue);
        }

        removeItem(i: number) {
            if (i > -1) {
                this.items.splice(i, 1);
            }
            this.updateEvent();
        }

        updateEvent() {
            this.$emit("input", {
                items: this.items,
                inputValue: this.inputValue
            });
        }

        itemType(item: TextOrImage) {
            if (typeof item == "string") {
                return "text";
            } else if (item.file && item.url) {
                return "image";
            }
        }

        clearField() {
            this.inputValue = "";
            this.updateEvent();
        }

        @Watch("inputValue")
        onInputValueUpdate() {
            this.updateEvent();
        }
    }
</script>

<style scoped lang="scss">
    @import "../style/constants";

    .pasted-image {
        max-width: 100%;
    }

    .item-display {
        display: flex;
        align-items: center;
        background-color: #fff;
        padding: 10pt;
        border-radius: 2pt;
        border: $border-width solid #888888;
    }

    .item-content {
        flex-grow: 1;
    }

    .item-actions {
        margin-left: 10pt;
        align-self: flex-start;
    }

    .content > * {
        margin-bottom: 8pt;
    }

    .content > *:last-child {
        margin-bottom: 0;
    }

    .divider {
        background: linear-gradient(transparent, $primary-dark);
        width: 100%;
        height: 30pt;
    }

    .content-wrapper {
        padding: 8pt;
        background-color: $primary-dark;
    }

    .delete-button {
        font-weight: bold;
        border: none;
        text-align: center;
        align-self: flex-start;
        margin-left: 10pt;
        user-select: none;
    }

    .delete-button:hover {
        cursor: pointer;
    }

    .input-field textarea {
        resize: none;
        border: none;
        padding: 8pt;
        min-width: 200pt;
        width: calc(100% - 16pt - 2pt);
        font-size: 1em;
        font-family: $font-family;
        color: inherit;
    }

    #text-image-paste-collector {
        border: $border-width solid $primary-darker;
        border-radius: 2pt;
        width: 100%;
        height: 100%;
        position: relative;
    }

    .add-item-instruction {
        font-family: monospace;
        font-size: 0.9em;
        opacity: 0.6;
        margin: 16pt 0 4pt;
    }

    .drag-modal {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        text-align: center;
        background: rgba(255, 255, 255, 0.8);
        pointer-events: none;
    }

    .drag-modal-center {
        text-align: center;
        margin: 8pt;
        border: 2pt dashed #cacaca;
        border-radius: 2pt;
        height: calc(100% - 16pt - 4pt);
        display: flex;
        align-items: center;
    }

    .drop-instruction {
        font-family: monospace;
        font-size: 1.2em;
        flex: 1;
        color: #888888;
    }
</style>
