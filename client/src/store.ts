import Vue from "vue";
import Vuex, { Store } from "vuex";

import { GeneratedProblem } from "./store";

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
    format: "static" | "generated";
    content: Widget[];
    // TODO using underscores because this is how it's done on the server. For now.
    setId: string;
    id: number;
}

// TODO: Move types to their own files
export interface GeneratedProblem extends Problem {
    solution: Widget[];
}

export interface StaticProblem extends Problem {
}

export interface StaticProblemSet {
    id: string;
    source: string;
    instructionContents: Widget[];
    answerContents: Widget[];
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
    file: File;
    url: string;
}

export type TextOrImage = string | ImageInfo;

export interface StaticProblemSetFormInfo {
    id: string;
    source: string;
    instructions: TextOrImage[];
    problems: TextOrImage[];
    answers: TextOrImage[];
}

export interface TextImagePasteCollectorState {
    items: TextOrImage[];
    inputValue: string;
}
