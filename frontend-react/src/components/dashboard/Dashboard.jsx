import React, { useEffect } from 'react'
import axiosInstance from '../../axiosInstance'

const Dashboard = () => {

    useEffect(() => {
        const fetchProtectedData = async () => {
            try {
                const response = await axiosInstance.get('/protected-view/')
                console.log('success: ', response.data)
            } catch (error) {
                console.error('Error fetching error', error)
            }
        }
        fetchProtectedData()
    }, [])
    
  return (
    <div className='container text-light'>Dashboard</div>
  )
}

export default Dashboard