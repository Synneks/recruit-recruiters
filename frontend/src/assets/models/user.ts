import { JobOffer } from './job-offer';

export class User{
    email: string;
    password: string;
    savedOffers: JobOffer[];
}