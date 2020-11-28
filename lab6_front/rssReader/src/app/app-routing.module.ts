import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {RssComponent} from './rss/rss.component';
import {NewsComponent} from './news/news.component';


const routes: Routes = [
    { path: 'rss', component: RssComponent },
    { path: 'news/:id', component: NewsComponent },
    { path: '**', redirectTo: '/rss' }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
