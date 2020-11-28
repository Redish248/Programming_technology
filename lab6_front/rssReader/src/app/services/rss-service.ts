import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {Observable} from 'rxjs';
import {Rss} from '../models/rss';

@Injectable({ providedIn: 'root' })
export class RssService {
    constructor(private http: HttpClient) { }

    getAllSites(): Observable<Rss[]> {
        return this.http.get<Rss[]>(`${environment.API_URL}/feed/get_sites`);
    }

    addSite(form: FormData): Observable<Rss> {
        return this.http.post<Rss>(`${environment.API_URL}/feed/add_sites`, form);
    }
}
