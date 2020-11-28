import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {RssService} from '../services/rss-service';
import {NewsList} from '../models/news';
import {MatSnackBar} from '@angular/material/snack-bar';

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
                private rssService: RssService,
                private snackBar: MatSnackBar) { }

    ngOnInit(): void {
        this.route.paramMap.subscribe(
            params => {
                this.siteId = Number(params.get('id'));
                this.page = 1;
                this.updateSite();
            }
        );
    }

    changePage(isNext: boolean): void {
        const newPage: number = this.page + (isNext ? 1 : -1);
        this.rssService.getNews(this.siteId, newPage).subscribe(news => {
          this.newsList = news;
          this.page = newPage;
        },
          error => this.snackBar.open('Error during parsing site news', 'Close', {
            duration: 5000,
          })
        );
    }

    updateSite(): void {
        this.rssService.updateNews(this.siteId).subscribe(news => {
            this.newsList = news;
            this.page = 1;
        },
          error => this.snackBar.open('Error during parsing site news', 'Close', {
            duration: 5000,
          })
        );
    }

}
