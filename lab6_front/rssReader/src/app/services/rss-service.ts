import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {Observable} from 'rxjs';
import {Rss} from '../models/rss';
import {NewsList} from '../models/news';

@Injectable({ providedIn: 'root' })
export class RssService {
    constructor(private http: HttpClient) { }

    getAllSites(): Observable<Rss[]> {
        return this.http.get<Rss[]>(`${environment.API_URL}/feed/get_sites`);
    }

    addSite(form: FormData): Observable<Rss> {
        return this.http.post<Rss>(`${environment.API_URL}/feed/add_sites`, form);
    }

    getNews(id: number, page: number): Observable<NewsList>{
        let params = new HttpParams();
        params = params.append('site_id', id.toString());
        params = params.append('page', page.toString());

        return this.http.get<NewsList>(`${environment.API_URL}/feed/get_news`, {params});
    }

    updateNews(id: number): Observable<NewsList>{
        let params = new HttpParams();
        params = params.append('site_id', id.toString());

        return this.http.get<NewsList>(`${environment.API_URL}/feed/update_news`, {params});
    }
}
