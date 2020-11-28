import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {RssService} from '../services/rss-service';
import {NewsList} from '../models/news';

@Component({
    selector: 'app-news',
    templateUrl: './news.component.html',
    styleUrls: ['./news.component.less']
})
export class NewsComponent implements OnInit {
    siteId: number;
    page: number;
    newsList: NewsList;

    constructor(private route: ActivatedRoute,
                private rssService: RssService) { }

    ngOnInit(): void {
        this.route.paramMap.subscribe(
            params => {
                this.siteId = Number(params.get('id'));
                this.page = 1;
                this.newsList = {isLastPage: false, news: [{id_news: 1, link: 'https://habr.com/ru/rss/interesting', site: 'kek',
                        description: 'kek <i>description</i>', published: new Date(), title: 'kek title'},
                        {id_news: 1, link: 'https://habr.com/ru/rss/interesting', site: 'kek',
                            description: 'kek <i>description</i>', published: new Date(), title: 'kek title'}]};
                /*this.rssService.getNews(this.siteId, this.page).subscribe(news => {
                    this.newsList = news;
                });*/
            }
        );
    }

    changePage(isNext: boolean): void {
        const newPage: number = this.page + (isNext ? 1 : -1);
        /*this.rssService.getNews(this.siteId, newPage).subscribe(news => {
                    this.newsList = news;
                    this.page = newPage;
                });*/
    }

    updateSite(): void {
        this.rssService.updateNews(this.siteId).subscribe(news => {
            this.newsList = news;
            this.page = 1;
        });
    }

}
