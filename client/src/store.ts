import {GeneratedProblem} from "./store";
import Vue from "vue";
import Vuex, {Store} from "vuex";

Vue.use(Vuex);

export const store: Store<AppState> = new Vuex.Store({
    state: {
        currentSession: undefined
    },
    mutations: {},
    actions: {},
});

export interface AppState {
    currentSession: CurrentSession | undefined;
}

export interface CurrentSession {
    problems: GeneratedProblem[];
}

export interface Problem {
    format: "static" | "generated"
    content: Widget[];
    // TODO using underscores because this is how it's done on the server. For now.
    setId: string
    id: number
}

// TODO: Move types to their own files
export interface GeneratedProblem extends Problem {
    solution: Widget[];
}

export interface StaticProblem extends Problem {
}

export interface Widget {
    options: WidgetOptions;
}

// tslint:disable-next-line:no-empty-interface
export interface WidgetOptions {
    type: "image" | "text";
}

export interface TextWidgetOptions extends WidgetOptions {
    text: string;
}

export interface ImageWidgetOptions extends WidgetOptions {
    id: string;
}

export interface ImageInfo {
    blob: File;
    url: string;
}

export type TextOrImage = string | ImageInfo;

export interface StaticProblemSetFormInfo {
    id: string;
    source: string;
    instructions: Array<TextOrImage>;
    problems: Array<TextOrImage>;
    answers: Array<TextOrImage>;
}