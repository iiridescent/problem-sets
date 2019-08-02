import {GeneratedProblem, Problem} from "@/store";

export class ProblemSetsAPI {
    // Need to figure out how to make this dynamic
    public static API_URL: string = `http://${window.location.hostname}:5000/api`;

    public static PROBLEM_SUFFIX: string = "problem";

    public async loadProblemsOfTypes(
        types: string | string[],
        count: number = 1
    ): Promise<Array<Problem | Error>> {
        const problems: Array<Problem | Error> = [];
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
            let problem: Problem | Error = await this.loadProblem(selectedType);

            problems.push(problem);
        }

        return problems;
    }

    public async loadProblem(type: string): Promise<GeneratedProblem | Error> {
        const response: Response = await fetch(
            `${ProblemSetsAPI.API_URL}/${ProblemSetsAPI.PROBLEM_SUFFIX}/${type}`
        );

        if (!response.ok) {
            console.log(response.statusText);

            const responseText = await response.text();

            return new Error(responseText)
        }

        return await response.json();
    }
}
