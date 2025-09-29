import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NxWelcomeComponent } from './nx-welcome.component';
import {BlockComponent} from './components/block.component'

@Component({
  standalone: true,
  imports: [NxWelcomeComponent, RouterModule, BlockComponent],
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'org.web.leanspire';
}
