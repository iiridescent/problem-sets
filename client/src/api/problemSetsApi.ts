import { GeneratedProblem } from "@/store";

export class ProblemSetsAPI {
    // Need to figure out how to make this dynamic
    public static API_URL: string = "localhost:5000/api";

    public static PROBLEM_SUFFIX: string = "problem";

    public async loadProblemsOfTypes(
        types: string | string[],
        count: number = 10
    ): Promise<GeneratedProblem[]> {
        const problems: GeneratedProblem[] = [];
        for (let i: number = 0; i < count; i++) {
            let selectedType: string;
            if (Array.isArray(types)) {
                const selectedIndex: number = Math.round(
                    Math.random() * (types.length - 1)
                );
                selectedType = types[selectedIndex];
            } else {
                selectedType = types;
            }

            const problem: GeneratedProblem = await this.loadProblem(selectedType);
            problems.push(problem);
        }

        return problems;
    }

    public async loadProblem(type: string): Promise<GeneratedProblem> {
        const response: Response = await fetch(
            `http://${ProblemSetsAPI.API_URL}/${ProblemSetsAPI.PROBLEM_SUFFIX}/${type}`
        );

        if (!response.ok) {
            const reason = `Failed to fetch problems. Status code: ${
                response.status
            }`;
            console.log(reason);

            return Promise.reject(reason);
        }

        // tslint:disable-next-line: no-unsafe-any
        const json: GeneratedProblem = await response.json();

        return json;

        // .then(response => {
        //     if (response.status !== 200) {
        //         console.log(
        //             'Looks like there was a problem. Status Code: ' +
        //                 response.status
        //         );
        //         return;
        //     }

        //     // Examine the text in the response
        //     response.json().then(function(data) {
        //         console.log(data);
        //     });
        // })
        // .catch(function(err) {
        //     console.log('Fetch Error :-S', err);
        // });
    }
}
