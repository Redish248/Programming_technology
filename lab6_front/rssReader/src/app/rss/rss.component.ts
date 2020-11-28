import {Component, OnInit} from '@angular/core';
import {RssService} from '../services/rss-service';
import {Rss} from '../models/rss';
import {Router} from '@angular/router';
import {MatSnackBar} from "@angular/material/snack-bar";

@Component({
    selector: 'app-rss',
    templateUrl: './rss.component.html',
    styleUrls: ['./rss.component.less']
})
export class RssComponent implements OnInit {

    sites: Rss[];
    newSiteUrl: string;

    constructor(private rssService: RssService,
                private router: Router,
                private snackBar: MatSnackBar) { }

    ngOnInit(): void {
        /*this.rssService.getAllSites().subscribe(sites => {
            this.sites = sites;
        });*/
        this.sites = [{id_site: 0, name: 'habr.com', url: 'https://habr.com/ru/rss/interesting'},
            {id_site: 1, name: 'news.yandex.ru', url: 'https://news.yandex.ru/volleyball.rss'}];
    }

    onSiteClick(id: number): void {
        this.router.navigate(['/news', id]);
    }

    addSite(): void {
        if (this.newSiteUrl) {
                const formData = new FormData();
                formData.append('url', this.newSiteUrl);
                this.rssService.addSite(formData).subscribe(newSite => {
                    this.sites.unshift(newSite);
                },
                    // todo: check error code
                    error => this.snackBar.open('This URL already added', 'Close', {
                        duration: 5000,
                    }));
            }
    }

}
