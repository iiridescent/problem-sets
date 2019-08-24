<template>
    <div id="static-set-form" @keyup.ctrl.shift.enter="onSubmit">
        <div class="submit-container">
            <button class="btn btn-lg" @click="onSubmit" :disabled="!canSubmit()">{{submitButtonText()}}<p class="shortcut"><span>ctrl</span>+<span>shift</span>+<span>enter</span></p></button>
        </div>
        <div class="set-id-field-container">
            <input class="card" v-model="newSetId" placeholder="set id"/>&nbsp;
            <div class="id-availability-indicator">
                {{getSetIdAvailabilityIndicator()}}
            </div>
            <br>
        </div>
        <label>
            <input class="source-field" v-model="source" placeholder="source"/>
        </label>
        <TextImagePasteCollector v-model="instructions" placeholder="instructions"/>
        <TextImagePasteCollector v-model="questions" placeholder="questions"/>
        <TextImagePasteCollector v-model="answers" placeholder="answer pages"/>
    </div>
</template>

<script lang="ts">
    import { StaticAPI } from "@/api/staticApi";
    import TextImagePasteCollector from "@/components/TextImagePasteCollector.vue";
    import { StaticProblemSetFormInfo, TextImagePasteCollectorState } from "@/store";
    import Component from "vue-class-component";
    import { Prop, Vue, Watch } from "vue-property-decorator";

    enum SetIDValidityState {
        AVAILABLE, UNAVAILABLE, LOADING, INVALID, EMPTY
    }

    @Component({
                   components: {
                       TextImagePasteCollector
                   }
               })
    export default class StaticSetForm extends Vue {
        @Prop() public setId: string | undefined;

        public instructions: TextImagePasteCollectorState = {
            inputValue: "",
            items: []
        };

        public questions: TextImagePasteCollectorState = {
            inputValue: "",
            items: []
        };

        public answers: TextImagePasteCollectorState = {
            inputValue: "",
            items: []
        };

        public newSetId: string = "";

        public source: string = "";

        private staticApi: StaticAPI = new StaticAPI();

        public setIdValidity: SetIDValidityState = SetIDValidityState.EMPTY;

        submitButtonText() {
            return this.setId == null ? "create" : "submit";
        }

        onSubmit() {
            if (this.setIdValidity !== SetIDValidityState.AVAILABLE) {
                alert(`set id '${this.newSetId}' isn't available`);
                return;
            }

            let formInfo: StaticProblemSetFormInfo = {
                instructions: this.instructions.items,
                problems: this.questions.items,
                answers: this.answers.items,
                source: this.source,
                id: this.newSetId,
            };

            this.staticApi.createStaticProblemSet(formInfo);
        }

        getSetIdAvailabilityIndicator() {
            switch (this.setIdValidity) {
                case SetIDValidityState.LOADING:
                    // Hourglass
                    return "\u23F3";
                case SetIDValidityState.AVAILABLE:
                    // White checkmark on green background
                    return "\u{2705}";
                case SetIDValidityState.UNAVAILABLE:
                    // Red 'X'
                    return "\u274C";
                case SetIDValidityState.INVALID:
                    // Red 'X'
                    return "\u274C (contains invalid characters)";
                default:
                    // Nothing
                    return "\u2205";
            }
        }

        canSubmit() {
            const isIdAvailable = this.setIdValidity === SetIDValidityState.AVAILABLE;
            const hasSource = this.source !== "";

            // Instructions must be submitted with ctrl + enter, which clears the instruction field
            // if the instruction field isn't empty, then it could mean the user wrote instructions but
            // forgot to submit them

            const isInstructionFieldEmpty = this.instructions.inputValue == "";

            // Note that we aren't requiring the instructions array to be nonzero.
            // Some problem types (like word problems) provide instructions inline with the problem.

            const hasQuestions = this.questions.items.length > 0;
            const hasAnswers = this.answers.items.length > 0;

            return isIdAvailable && hasSource && isInstructionFieldEmpty && hasQuestions && hasAnswers;
        }

        @Watch("newSetId")
        async onNewSetIdChange() {
            if (this.newSetId == "") {
                this.setIdValidity = SetIDValidityState.EMPTY;
                return;
            }

            const validRegex = /([a-zA-Z0-9-]+)/g;

            let cleanedNewSetId = this.newSetId.replace(/ /g, "-").toLowerCase();

            const newSetIdMatched = cleanedNewSetId.match(validRegex);

            if (newSetIdMatched === null || newSetIdMatched.length == 0) {
                this.setIdValidity = SetIDValidityState.INVALID;
                return;
            }

            cleanedNewSetId = newSetIdMatched.join("");

            this.newSetId = cleanedNewSetId;

            if (!/^([a-zA-Z0-9-]+)$/.test(this.newSetId)) {
                this.setIdValidity = SetIDValidityState.INVALID;
                return;
            }

            const isSetIdAvailable = await this.staticApi.checkStaticProblemSetIdAvailable(this.newSetId);

            this.setIdValidity = isSetIdAvailable ? SetIDValidityState.AVAILABLE : SetIDValidityState.UNAVAILABLE;
        }
    }
</script>

<style scoped lang="scss">
    @import "../style/constants";

    .set-id-field-container {
        display: flex;
        flex-wrap: nowrap;
        align-items: center;
    }

    .set-id-field-container input {
        flex-grow: 1;
    }

    #static-set-form > * {
        margin: 8pt 0;
    }

    .source-field {
        width: calc(100% - 16pt);
    }

    input {
        border: $border-width solid $primary-darker;
        border-radius: 2pt;
        padding: 8pt;
        min-width: 200pt;
        font-size: 1em;
        color: inherit;
        font-family: $font-family;
    }

    .id-availability-indicator {
        width: 30pt;
        text-align: center;
    }

    .submit-container {
        display: flex;
        align-items: center;
    }

</style>
