import apiClient from '$lib/config/axios.config';

export class PriceRepository {
    async getPrice(
        quality: string,
        garageSize: string,
        exteriorQuality: string,
        livingArea: string,
        bathrooms: string,
        kitchenQuality: string,
        yearBuilt: string,
        firstFloorArea: string,
        basementQuality: string,
        fireplace: string
    ): Promise<string> {
        return new Promise((resolve, reject) => {
            apiClient.post('/predict', {
                OverallQual: quality,
                GarageCars: garageSize,
                ExterQual: exteriorQuality,
                GrLivArea: livingArea,
                FullBath: bathrooms,
                KitchenQual: kitchenQuality,
                YearBuilt: yearBuilt,
                FirstFlrSF: firstFloorArea,
                BsmtQual: basementQuality,
                Fireplaces: fireplace,
            })
                .then(response => {
                    resolve(response.data.price);
                })
                .catch(error => {
                    reject(error?.response?.data || 'An error occurred while retrieving price');
                });
        });
    }
}
