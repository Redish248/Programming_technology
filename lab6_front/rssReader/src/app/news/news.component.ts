import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';

@Component({
    selector: 'app-news',
    templateUrl: './news.component.html',
    styleUrls: ['./news.component.less']
})
export class NewsComponent implements OnInit {
    siteId: number;

    constructor(private route: ActivatedRoute) { }

    ngOnInit(): void {
        this.route.paramMap.subscribe(
            params => {
                this.siteId = Number(params.get('id'));
                // request
            }
        );
    }

}
