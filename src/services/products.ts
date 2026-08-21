import { apiService, ApiError } from './api'

export interface Product {
  id: number
  title: string  // Backend uses 'title' not 'name'
  description: string
  price: string  // Backend returns decimal as string
  category: number  // Backend uses category ID
  image: string  // Backend uses single 'image' not 'images' array
  condition: string
  year: number | null
  is_available: boolean
  seller: number
  created_at: string
  updated_at: string
}

export interface Category {
  id: number
  name: string
  description?: string
  products_count?: number
}

export interface CreateProductData {
  title: string
  description: string
  price: number
  category: number  // Category ID
  condition?: string
  year?: number
  image?: File
}

export interface UpdateProductData extends Partial<CreateProductData> {
  status?: 'active' | 'inactive'
}

// Products Service
class ProductsService {
  
  // Get all products
  async getProducts(params?: {
    page?: number
    limit?: number
    category?: string
    seller?: number
    status?: string
  }): Promise<Product[]> {
    try {
      const searchParams = new URLSearchParams()
      if (params?.page) searchParams.set('page', params.page.toString())
      if (params?.limit) searchParams.set('limit', params.limit.toString())
      if (params?.category) searchParams.set('category', params.category)
      if (params?.seller) searchParams.set('seller', params.seller.toString())
      if (params?.status) searchParams.set('status', params.status)

      const queryString = searchParams.toString()
      const endpoint = queryString ? `/products/?${queryString}` : '/products/'
      
      // Backend returns array directly, not paginated
      return await apiService.get<Product[]>(endpoint)
    } catch (error) {
      // Silent fail - return empty array
      return []
    }
  }

  // Get single product
  async getProduct(id: number): Promise<Product> {
    try {
      return await apiService.get<Product>(`/products/${id}/`)
    } catch (error) {
      throw new ApiError('Failed to fetch product', 500, error)
    }
  }

  // Create product
  async createProduct(data: CreateProductData): Promise<Product> {
    try {
      if (data.image) {
        // Handle file upload
        const formData = new FormData()
        formData.append('title', data.title)
        formData.append('description', data.description)
        formData.append('price', data.price.toString())
        formData.append('category', data.category.toString())
        if (data.condition) formData.append('condition', data.condition)
        if (data.year) formData.append('year', data.year.toString())
        formData.append('image', data.image)

        return await apiService.uploadFile<Product>('/products/', formData)
      } else {
        // Regular JSON post
        const { image, ...productData } = data
        return await apiService.post<Product>('/products/', productData)
      }
    } catch (error) {
      throw new ApiError('Failed to create product', 500, error)
    }
  }

  // Update product
  async updateProduct(id: number, data: UpdateProductData): Promise<Product> {
    try {
      if (data.image) {
        // Handle file upload
        const formData = new FormData()
        Object.entries(data).forEach(([key, value]) => {
          if (key !== 'image' && value !== undefined) {
            formData.append(key, value.toString())
          }
        })
        formData.append('image', data.image)

        return await apiService.uploadFile<Product>(`/products/${id}/`, formData)
      } else {
        // Regular JSON patch
        const { image, ...productData } = data
        return await apiService.patch<Product>(`/products/${id}/`, productData)
      }
    } catch (error) {
      throw new ApiError('Failed to update product', 500, error)
    }
  }

  // Delete product
  async deleteProduct(id: number): Promise<void> {
    try {
      await apiService.delete(`/products/${id}/`)
    } catch (error) {
      throw new ApiError('Failed to delete product', 500, error)
    }
  }

  // Get categories
  async getCategories(): Promise<Category[]> {
    try {
      return await apiService.get<Category[]>('/categories/')
    } catch (error) {
      throw new ApiError('Failed to fetch categories', 500, error)
    }
  }

  // Create category
  async createCategory(data: { name: string; description?: string }): Promise<Category> {
    try {
      return await apiService.post<Category>('/categories/', data)
    } catch (error) {
      throw new ApiError('Failed to create category', 500, error)
    }
  }

  // Update category
  async updateCategory(id: number, data: { name?: string; description?: string }): Promise<Category> {
    try {
      return await apiService.patch<Category>(`/categories/${id}/`, data)
    } catch (error) {
      throw new ApiError('Failed to update category', 500, error)
    }
  }

  // Delete category
  async deleteCategory(id: number): Promise<void> {
    try {
      await apiService.delete(`/categories/${id}/`)
    } catch (error) {
      throw new ApiError('Failed to delete category', 500, error)
    }
  }
}

// Export singleton instance
export const productsService = new ProductsService()