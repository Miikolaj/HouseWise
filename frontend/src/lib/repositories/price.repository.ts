import apiClient from '$lib/config/axios.config';

export class PriceRepository {
    async getPrice(area: string, bedrooms: string, bathrooms: string, floors: string, condition: string, location: string, year: string, garage: boolean) :Promise<string> {
        return new Promise((resolve, reject) => {
            apiClient.post('/price', {area, bedrooms, bathrooms, floors, condition, location, year, garage})
                .then(response => {
                    resolve(response.data.price);
                })
                .catch(error => {
                    reject(error?.response?.data || 'An error occurred while retrieving price');
                });
        });
    }
}