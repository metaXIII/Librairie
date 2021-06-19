import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';
import { PastLaucnhesListGQL } from '../services/spacexGraphql.services';
import {map} from "rxjs/operators"

@Component({
  selector: 'app-launch-list',
  templateUrl: './launch-list.component.html',
  styleUrls: ['./launch-list.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class LaunchListComponent implements OnInit {

  constructor(private pastLaunchesServices: PastLaucnhesListGQL) { }

  pastLaunches$ = this.pastLaunchesServices
  .fetch({limit: 30})
  .pipe(
    map(
    res => res.data.launchesPast
  ));

  ngOnInit(): void {
  }

}
