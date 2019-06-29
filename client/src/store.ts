import { Problem } from './store';
import Vue from 'vue';
import Vuex, { Store } from 'vuex';

Vue.use(Vuex);

export const store: Store<AppState> = new Vuex.Store({
  state: {
      currentSession: undefined
  },
  mutations: {

  },
  actions: {

  },
});

export interface AppState {
  currentSession: CurrentSession | undefined;
}

export interface CurrentSession {
  problems: Problem[];
}
// TODO: Move types to their own files
export interface Problem {
  content: Widget[];
  solution: Widget[];
}

export interface Widget {
  options: WidgetOptions;
}

// tslint:disable-next-line:no-empty-interface
export interface WidgetOptions {}

export interface TextWidgetOptions extends WidgetOptions {
  text: string;
}