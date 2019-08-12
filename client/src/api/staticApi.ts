import {StaticProblemSetFormInfo, TextOrImage, StaticProblemSet} from "@/store";

export class StaticAPI {

    public static API_URL: string = `http://${window.location.hostname}:5000/api/static`;


    public async getStaticProblemSet(id: string): Promise<StaticProblemSet | string> {
        let response = await fetch(`${StaticAPI.API_URL}/sets/${id}`, {method: "GET"});

        if (!response.ok) {
            return response.statusText
        }

        return await response.json()
    }


    public async getStaticProblemSets(): Promise<StaticProblemSet[] | string> {
        let response = await fetch(`${StaticAPI.API_URL}/sets`, {method: "GET"});

        if (!response.ok) {
            return response.statusText
        }

        return await response.json()
    }

    public async deleteStaticProblemSet(id: string): Promise<boolean> {
        let response = await fetch(`${StaticAPI.API_URL}/sets/${id}`, {method: "DELETE"});

        return response.ok
    }


    public async createStaticProblemSet(formInfo: StaticProblemSetFormInfo) {
        const formData = new FormData();

        formData.append('id', formInfo.id);
        formData.append('source', formInfo.source);

        let instructions = formInfo.instructions;
        let answers = formInfo.answers;

        StaticAPI.addAllTextOrImagesToFormData('instructions', instructions, formData);
        StaticAPI.addAllTextOrImagesToFormData('answers', answers, formData);

        const options = {
            method: 'POST',
            body: formData,
        };

        let response = await fetch(`${StaticAPI.API_URL}/sets`, options);

        if (!response.ok) {
            return response.statusText
        }

        let problems = formInfo.problems

        for (let problem of problems) {
            this.createProblem(formInfo.id, problem)
        }
    }

    public async createProblem(setId: string, content: TextOrImage) {
        if (typeof content === "string") {
            // We're not going to support text-based static questions right now
            return;
        }

        const formData = new FormData();

        formData.append('setId', setId);
        formData.append('content', content.blob)

        const options = {
            method: 'POST',
            body: formData,
        };

        let response = await fetch(`${StaticAPI.API_URL}/problems`, options);

        if (!response.ok) {
            console.log(response.statusText)
        }
    }

    public async setProblemUsed(id: number, used: boolean) {
        console.log(used)
        const options = {
            method: 'PATCH',
            body: JSON.stringify({"used": used}),
            headers: {
                'Content-Type': 'application/json',
            }
        };
        let response = await fetch(`${StaticAPI.API_URL}/problems/${id}`, options);
        return response.statusText
    }

    private static addAllTextOrImagesToFormData(key: string, contentList: Array<TextOrImage>, formData: FormData) {
        for (let i = 0; i < contentList.length; i++) {
            let item = contentList[i];

            let formDataItem: StaticContentFormDataItem;

            if (typeof item === "string") {
                formDataItem = {
                    type: "text",
                    value: item
                };
            } else if (item.blob && item.url) {
                formDataItem = {
                    type: "image",
                };

                formData.append(key + 'Images[]', item.blob)
            } else {
                continue
            }

            formData.append(key + '[]', JSON.stringify(formDataItem))
        }
    }
}

interface StaticContentFormDataItem {
    type: 'text' | 'image';
    // Null if is image
    value?: string;
}
