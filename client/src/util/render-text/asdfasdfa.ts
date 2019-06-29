/* eslint no-console:0 */

import katex, { KatexOptions } from "katex";
import splitAtDelimiters from "./splitAtDelimiters";

interface DelimiterSplitData {
    type: string;
    data: string;

    rawData?: string;
    display?: boolean;
}



function splitWithDelimiters(text: string, delimiters: RenderMathInElementSpecificOptionsDelimiters[]): DelimiterSplitData[] {
    let data: DelimiterSplitData[] = [{type: "text", data: text}];
    for (let i = 0; i < delimiters.length; i++) {
        const delimiter = delimiters[i];
        data = splitAtDelimiters(
            data, delimiter.left, delimiter.right,
            delimiter.display || false);
    }
    return data;
};

/* Note: optionsCopy is mutated by this method. If it is ever exposed in the
 * API, we should copy it before mutating.
 */
const renderMathInText = function(text: string, options: RenderMathInElementOptions) {

    const optionsCopy: RenderMathInElementOptions = {};

    // Object.assign(optionsCopy, option)
    for (const option in options) {
        if (options.hasOwnProperty(option)) {
            // tslint:disable-next-line:ban-ts-ignore
            // @ts-ignore
            optionsCopy[option] = options[option];
        }
    }

    // default options
    optionsCopy.delimiters = optionsCopy.delimiters || [
        {left: "$$", right: "$$", display: true},
        {left: "\\(", right: "\\)", display: false},
        // LaTeX uses $…$, but it ruins the display of normal `$` in text:
        // {left: "$", right: "$", display: false},

        //  \[…\] must come last in this array. Otherwise, renderMathInElement
        //  will search for \[ before it searches for $$ or  \(
        // That makes it susceptible to finding a \\[0.3em] row delimiter and
        // treating it as if it were the start of a KaTeX math zone.
        {left: "\\[", right: "\\]", display: true},
    ];
    optionsCopy.ignoredTags = optionsCopy.ignoredTags || [
        "script", "noscript", "style", "textarea", "pre", "code",
    ];
    optionsCopy.ignoredClasses = optionsCopy.ignoredClasses || [];
    optionsCopy.errorCallback = optionsCopy.errorCallback || console.error;

    // Enable sharing of global macros defined via `\gdef` between different
    // math elements within a single call to `renderMathInElement`.
    optionsCopy.macros = optionsCopy.macros || {};

    const data: = splitWithDelimiters(text, optionsCopy.delimiters);
    const fragment = document.createDocumentFragment();

    for (let i = 0; i < data.length; i++) {
        if (data[i].type === "text") {
            fragment.appendChild(document.createTextNode(data[i].data));
        } else {
            const span = document.createElement("span");
            let math = data[i].data;
            // Override any display mode defined in the settings with that
            // defined by the text itself
            optionsCopy.displayMode = data[i].display;
            try {
                // if (optionsCopy.preProcess) {
                //     math = optionsCopy.preProcess(math);
                // }
                katex.render(math, span, optionsCopy);
            } catch (e) {
                if (!(e instanceof katex.ParseError)) {
                    throw e;
                }
                optionsCopy.errorCallback(
                    "KaTeX auto-render: Failed to parse `" + data[i].data +
                    "` with ",
                    e
                );
                fragment.appendChild(document.createTextNode(data[i].rawData));
                continue;
            }
            fragment.appendChild(span);
        }
    }

    return fragment;
};