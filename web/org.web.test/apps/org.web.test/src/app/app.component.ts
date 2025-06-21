import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NxWelcomeComponent } from './nx-welcome.component';
import { ProcessComponent  } from './shared/components/processComp/process-block.component';

@Component({
  standalone: true,
  // imports: [NxWelcomeComponent, RouterModule],
  imports: [ProcessComponent, RouterModule, NxWelcomeComponent],
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'org.web.test';
}
