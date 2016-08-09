class Api::KeystrokeTypesController < ApplicationController
  before_action :set_keystroke_type, only: :show

  def index
    @keystroke_types = KeystrokeType.all

    render json: @keystroke_types
  end

  def show
    render json: @keystroke_type
  end

  def create
    @keystroke_type = KeystrokeType.new(keystroke_type_params)

    if @keystroke_type.save
      render json: @keystroke_type, status: :created
    else
      render json: @keystroke_type.errors, status: :unprocessable_entity
    end
  end

  private

  def set_keystroke_type
    @keystroke_type = KeystrokeType.find(params[:id])
  end

  def keystroke_type_params
    params.require(:keystroke_type).permit(:name)
  end
end
