class Api::ElementTypesController < ApplicationController
  before_action :set_element_type, only: :show

  def index
    @element_types = ElementType.all

    render json: @element_types
  end

  def show
    render json: @element_type
  end

  def create
    @element_type = ElementType.new(element_type_params)

    if @element_type.save
      render json: @element_type, status: :created
    else
      render json: @element_type.errors, status: :unprocessable_entity
    end
  end

  private

  def set_element_type
    @element_type = ElementType.find(params[:id])
  end

  def element_type_params
    params.require(:element_type).permit(:id, :name)
  end
end
