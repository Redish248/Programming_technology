export class News {
    id_news: number;
    site: string;
    title: string;
    link: string;
    description: string;
    published: Date;
}

export class NewsList {
    news: News[];
    isLastPage: boolean;
}
