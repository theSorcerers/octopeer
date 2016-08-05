class Api::V1::UsersController < ApplicationController
  def index
    render json: User.all
  end

  def show
    render json: User.find(params[:id])
  end

  def create
    user = User.new(user_params)
    if user.save
      render json: user
    else
      render json: { errors: user.errors }
    end
  end

  private

  def user_params
    params.require(:user).permit(:username)
  end
end
